//
// Created by paulyhedral on 6/25/21.
//

import Fluent
import Vapor

public final class System : Model {
    public static let schema = LibraryModel.System.v20210625.schemaName

    @ID
    public var id : UUID?

    @Timestamp(key: Volume.v20210620.createdAt, on: .create)
    public var createdAt : Date?

    @Timestamp(key: Volume.v20210620.updatedAt, on: .update)
    public var updatedAt : Date?

    @Field(key: LibraryModel.System.v20210625.gameSystemIdentifier)
    public var gameSystemIdentifier : String

    @Field(key: LibraryModel.System.v20210625.editionIdentifier)
    public var editionIdentifier : String

    @Children(for: \.$system)
    public var volumes : [Volume]

    public init() {}

    public init(id : UUID? = nil, gameSystemIdentifier : String, editionIdentifier : String) {
        self.id = id
        self.gameSystemIdentifier = gameSystemIdentifier
        self.editionIdentifier = editionIdentifier
    }
}
