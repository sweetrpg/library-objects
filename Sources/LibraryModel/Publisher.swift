//
// Publisher.swift
// Copyright (c) 2021 Paul Schifferer.
//

import Fluent
import Vapor


public final class Publisher : Model {
    public static let schema = Publisher.v20210625.schemaName

    @ID
    public var id : UUID?

    @Timestamp(key: Publisher.v20210625.createdAt, on: .create)
    public var createdAt : Date?

    @Timestamp(key: Publisher.v20210625.updatedAt, on: .update)
    public var updatedAt : Date?

    @Field(key: Publisher.v20210625.name)
    public var name : String

    @Timestamp(key: Publisher.v20210625.deletedAt, on: .delete)
    public var deletedAt : Date?

    public init() {
    }

    public init(id : UUID? = nil, name : String) {
        self.id = id
        self.name = name
    }

}

extension Publisher : Content {}
